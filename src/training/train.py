"""
Training loop script for Robot Soccer SSL Tactical Prediction.

This module provides standard PyTorch training and validation loops,
using Adam optimizer, Cross-Entropy Loss, and basic model checkpointing.
"""

import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from tqdm import tqdm

# Import the model - assuming it's run from the root of the project
# from src.models.lstm_model import TacticalLSTM
# from src.features.build_features import SSLSlidingWindowDataset

def get_device() -> torch.device:
    """
    Determines the best available device for PyTorch.
    
    Returns:
        torch.device: The selected PyTorch device (CUDA, MPS, or CPU).
    """
    if torch.cuda.is_available():
        return torch.device("cuda")
    elif torch.backends.mps.is_available():
        return torch.device("mps")
    else:
        return torch.device("cpu")

def train_one_epoch(
    model: nn.Module, 
    dataloader: DataLoader, 
    criterion: nn.Module, 
    optimizer: optim.Optimizer, 
    device: torch.device
) -> float:
    """
    Trains the model for one epoch.
    
    Args:
        model (nn.Module): The PyTorch model to train.
        dataloader (DataLoader): DataLoader providing the training data.
        criterion (nn.Module): Loss function.
        optimizer (optim.Optimizer): Optimizer.
        device (torch.device): Device to run computation on.
        
    Returns:
        float: Average training loss for the epoch.
    """
    model.train()
    running_loss = 0.0
    
    progress_bar = tqdm(dataloader, desc="Training", leave=False)
    for inputs, targets in progress_bar:
        inputs, targets = inputs.to(device), targets.to(device)
        
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item() * inputs.size(0)
        progress_bar.set_postfix({'loss': loss.item()})
        
    return running_loss / len(dataloader.dataset)

def validate(
    model: nn.Module, 
    dataloader: DataLoader, 
    criterion: nn.Module, 
    device: torch.device
) -> tuple[float, float]:
    """
    Evaluates the model on the validation set.
    
    Args:
        model (nn.Module): The PyTorch model.
        dataloader (DataLoader): DataLoader providing the validation data.
        criterion (nn.Module): Loss function.
        device (torch.device): Device to run computation on.
        
    Returns:
        tuple[float, float]: Average validation loss and accuracy.
    """
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0
    
    with torch.no_grad():
        for inputs, targets in tqdm(dataloader, desc="Validation", leave=False):
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            
            running_loss += loss.item() * inputs.size(0)
            _, predicted = torch.max(outputs, 1)
            total += targets.size(0)
            correct += (predicted == targets).sum().item()
            
    val_loss = running_loss / len(dataloader.dataset)
    val_accuracy = correct / total if total > 0 else 0.0
    
    return val_loss, val_accuracy

def main():
    """
    Main training execution function.
    """
    device = get_device()
    print(f"Using device: {device}")
    
    # Configuration (mock setup for demonstration)
    num_epochs = 10
    learning_rate = 0.001
    model_save_path = "models/tactical_lstm.pth"
    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
    
    print("Note: DataLoader and Model initialization requires real data. Skipping actual loop.")
    
    # Example setup logic
    """
    model = TacticalLSTM(input_size=10, hidden_size=64, num_layers=2, num_classes=5).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    best_val_loss = float('inf')
    
    for epoch in range(num_epochs):
        print(f"Epoch {epoch+1}/{num_epochs}")
        train_loss = train_one_epoch(model, train_loader, criterion, optimizer, device)
        val_loss, val_accuracy = validate(model, val_loader, criterion, device)
        
        print(f"Train Loss: {train_loss:.4f} | Val Loss: {val_loss:.4f} | Val Acc: {val_accuracy:.4f}")
        
        # Checkpoint model
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            torch.save(model.state_dict(), model_save_path)
            print(f"Model saved to {model_save_path}")
    """

if __name__ == "__main__":
    main()
