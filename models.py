import torch
import torch.nn as nn

class TrafficGenerator(nn.Module):
    def __init__(self, latent_dim=32, num_features=128):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.BatchNorm1d(64),
            nn.ReLU(True),
            nn.Linear(64, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(True),
            nn.Linear(128, num_features),
            nn.Tanh()
        )
    def forward(self, z): 
        return self.model(z)