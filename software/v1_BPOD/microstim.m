function microstim
global BpodSystem
S = BpodSystem.ProtocolSettings;

%% Define parameters


% Might want to set the protocol settings before hand but for now
if isempty(fieldnames(S))
    S.GUI.RewardAmount = 5; % TODO check if this is correct for 5uL
    S.ResponseWindow = 1.0;
%     S.GUI.Pairing = 0;
%     S.GUIMeta.Pairing.Style = 'checkbox';
end
% Initialize GUI and Notebook
BpodParameterGUI('init', S);
% BpodNotebook('init');
MaxTrials = 150;
%TrialTypes = ceil(rand(1, MaxTrials+50)*2); % Either 1=test or 2=catch
TrialTypes = randsrc(1, MaxTrials+50, [1 2; 0.6 0.4]);
% TODO Calibrate this
R = GetValveTimes(S.GUI.RewardAmount, [1]); % Return the valve-open duration in seconds for valve 1
ValveTime = R(1);

%% Define stimulus
% W = BpodWavePlayer('COM3'); 
% W.SamplingRate = 10000; % Set the sampling rate to 1 kHz

%% Initialize plots
% Lickingplot?
% https://sanworks.io/forum/showthread.php?tid=39&highlight=response

% Outcome plot showing hits and misses
BpodSystem.ProtocolFigures.OutcomePlotFig = figure('Position', [0 480 1000 250],'name','Outcome plot',... 
    'numbertitle','off', 'MenuBar', 'none', 'Resize', 'off'); % Create a figure for the outcome plot
BpodSystem.GUIHandles.OutcomePlot = axes('Position', [.075 .3 .89 .6]); % Create axes for the trial type outcome plot
TrialTypeOutcomePlot(BpodSystem.GUIHandles.OutcomePlot,'init',TrialTypes);

% Response time for recent trials
BpodSystem.ProtocolFigures.MyPlotFig = figure('Position', [0 750 1000 250],'name','MyPlotFig');


%% Main Loop
disp("-------------STARTING PROTOCOL---------------");
for currentTrial = 1:MaxTrials  
    %S = BpodParameterGUI('sync', S); % Synch settings

    % Configure settings for pairing or testing trials
%     switch S.GUI.Pairing
%         case 0 % This means we are not pairing but testing
%             AfterStim = 'WaitForLick';
%             disp('Testing');
%         case 1 % Pairing
%             AfterStim = 'Reward';
%             disp('Pairing');
%     end
    
    switch TrialTypes(currentTrial)
        case 1 %Testing trial
            %AfterLick = {'Tup', 'exit', 'Port1In', 'Reward', 'Port1Out', 'Reward'};
            %Stimulus = {'BNCState', 3}; % Sets both BNC 1 and 2 to high to trigger stim and camera
            Stimulus = {'Serial1', '1', 'BNCState', 1}; % Stimulation and camera
            Reward = {'BNCState', 2}; 
            dotColor = 'black';
            disp('Test');
        case 2
            %AfterLick = {'Tup', 'exit'};
            Stimulus = {'BNCState', 1}; % Just camera
            Reward = {};
            dotColor = 'white';
            disp('Catch');
    end

    % Construct the StateMatrix
    sma = NewStateMatrix();
    sma = AddState(sma, 'Name', 'WaitForStim', ...
        'Timer', randi([4, 6]), ... %TODO Hardcoded
        'StateChangeConditions', {'BNC1Low', 'Timeout', 'BNC1High', 'Timeout', 'Tup', 'Stimulus'}, ...
        'OutputActions', {});
    
    sma = AddState(sma, 'Name', 'Timeout', ...
        'Timer', 0, ...
        'StateChangeConditions', {'Tup', 'WaitForStim'}, ...
        'OutputActions', {});

    sma = AddState(sma, 'Name', 'Stimulus', ...
        'Timer', 0.2, ...
        'StateChangeConditions', {'Tup', 'WaitForLick'}, ...   % If Tup this could go into delay if implemented
        'OutputActions', Stimulus); 
       
    sma = AddState(sma, 'Name', 'WaitForLick', ...
        'Timer', 1.5, ...
        'StateChangeConditions', {'Tup', 'exit', 'BNC1Low', 'Reward', 'BNC1High', 'Reward'}, ...  %AfterLick
        'OutputActions', {}); %TODO this doesnt always trigger properly

    sma = AddState(sma, 'Name', 'Reward', ...
        'Timer', 2, ...
        'StateChangeConditions', {'Tup', 'exit'}, ...
        'OutputActions', Reward); %TODO check what this corresponds to

    % Send StateMatrix to Bpod
    SendStateMachine(sma);
    RawEvents = RunStateMachine; 

    if ~isempty(fieldnames(RawEvents)) % If trial data was returned
        BpodSystem.Data = AddTrialEvents(BpodSystem.Data, RawEvents); 
        BpodSystem.Data.TrialSettings(currentTrial) = S; % Adds the settings used for the current trial to the Data struct (to be saved after the trial ends)
        BpodSystem.Data.TrialTypes(currentTrial) = TrialTypes(currentTrial); % Adds the trial type of the current trial to data
        SaveBpodSessionData; % Saves the field BpodSystem.Data to the current data file
    end
    
    % Handle pause and exit conditions
    HandlePauseCondition;
    if BpodSystem.Status.BeingUsed == 0
       return
    end


    %% Update plots
    Outcomes = zeros(1,BpodSystem.Data.nTrials);
    for x = 1:BpodSystem.Data.nTrials
        if ~isnan(BpodSystem.Data.RawEvents.Trial{x}.States.Reward(1))
            Outcomes(x) = 1; 
            RT = BpodSystem.Data.RawEvents.Trial{x}.States.WaitForLick(2) - BpodSystem.Data.RawEvents.Trial{x}.States.WaitForLick(1);
        else
            Outcomes(x) = 0;
            RT = 0;
        end
    end

    % Correct or incorrect
    %disp(BpodSystem.GUIHandles.OutcomePlot);
    TrialTypeOutcomePlot(BpodSystem.GUIHandles.OutcomePlot,'update',...
        BpodSystem.Data.nTrials+1,TrialTypes,Outcomes);
    
    % Response time figure
    figure(BpodSystem.ProtocolFigures.MyPlotFig);
    scatter(currentTrial, RT, 50,'filled', dotColor);
    line(currentTrial,RT)
    ylabel('Response Time (s)');
    ylim([0, 1.5])
    xlabel('Trial #');
    xlim([currentTrial-10, currentTrial])
    grid on;
    hold on;
         
end
