"""
LSTM model definition for Robot Soccer SSL Tactical Prediction.

This module implements a basic PyTorch LSTM network designed for
multivariate time-series classification of tactical behaviors.
"""

import torch
import torch.nn as nn

class TacticalLSTM(nn.Module):
    """
    An LSTM-based neural network for tactical prediction from sequence data.
    
    The model takes input sequences of shape (Batch, Sequence Length, Features)
    and predicts a tactical class.
    """
    
    def __init__(self, input_size: int, hidden_size: int, num_layers: int, num_classes: int, dropout: float = 0.2):
        """
        Initializes the LSTM model.
        
        Args:
            input_size (int): The number of features in the input data.
            hidden_size (int): The number of features in the hidden state of the LSTM.
            num_layers (int): Number of recurrent layers.
            num_classes (int): Number of output classes for classification.
            dropout (float): Dropout probability for LSTM layers (if num_layers > 1).
        """
        super(TacticalLSTM, self).__init__()
        
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        # LSTM layer
        # batch_first=True implies input shape is (batch, seq, feature)
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0
        )
        
        # Fully connected output layer
        self.fc = nn.Linear(hidden_size, num_classes)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass of the model.
        
        Args:
            x (torch.Tensor): Input tensor of shape (batch_size, sequence_length, input_size).
            
        Returns:
            torch.Tensor: Output logits of shape (batch_size, num_classes).
        """
        # Initialize hidden and cell states dynamically based on batch size and device
        batch_size = x.size(0)
        h0 = torch.zeros(self.num_layers, batch_size, self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, batch_size, self.hidden_size).to(x.device)
        
        # Forward propagate LSTM
        # out: tensor of shape (batch_size, seq_length, hidden_size)
        out, (hn, cn) = self.lstm(x, (h0, c0))
        
        # Decode the hidden state of the last time step
        # out[:, -1, :] gets the output of the last time step for all items in the batch
        out = self.fc(out[:, -1, :])
        
        return out
