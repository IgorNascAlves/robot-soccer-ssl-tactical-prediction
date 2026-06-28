"""
Feature engineering script for Robot Soccer SSL Tactical Prediction.

This module provides a PyTorch Dataset class that transforms tabular
time-series telemetry data into sliding windows (tensors) suitable for
sequential modeling with Deep Learning.
"""

import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset

class SSLSlidingWindowDataset(Dataset):
    """
    A PyTorch Dataset that generates sliding windows from time-series DataFrame.
    """
    
    def __init__(self, dataframe: pd.DataFrame, window_size: int, step_size: int = 1, target_col: str = None):
        """
        Initializes the dataset.
        
        Args:
            dataframe (pd.DataFrame): The input tabular data containing telemetry.
            window_size (int): The number of time steps (T) in each window.
            step_size (int): The stride between consecutive windows.
            target_col (str, optional): The name of the column containing the target labels.
                If None, the dataset will only return features.
        """
        self.window_size = window_size
        self.step_size = step_size
        self.target_col = target_col
        
        # Separate features and targets
        if self.target_col and self.target_col in dataframe.columns:
            self.features = dataframe.drop(columns=[self.target_col]).values
            self.targets = dataframe[self.target_col].values
        else:
            self.features = dataframe.values
            self.targets = None
            
        # Ensure numerical data is represented as float32 for PyTorch
        self.features = self.features.astype(np.float32)
        
        # Calculate valid start indices for windows
        self.indices = np.arange(0, len(self.features) - self.window_size + 1, self.step_size)
        
    def __len__(self) -> int:
        """
        Returns the total number of windows in the dataset.
        
        Returns:
            int: Total number of samples.
        """
        return len(self.indices)
        
    def __getitem__(self, idx: int):
        """
        Retrieves a single sliding window and its corresponding label (if any).
        
        Args:
            idx (int): Index of the window to retrieve.
            
        Returns:
            tuple: (features_tensor, target_tensor) or just features_tensor.
                - features_tensor shape: (window_size, num_features)
        """
        start_idx = self.indices[idx]
        end_idx = start_idx + self.window_size
        
        x = torch.tensor(self.features[start_idx:end_idx], dtype=torch.float32)
        
        if self.targets is not None:
            # Typically, for sequence classification, the target might be the label 
            # at the end of the window or a single label for the whole window.
            y = torch.tensor(self.targets[end_idx - 1], dtype=torch.long)
            return x, y
            
        return x
