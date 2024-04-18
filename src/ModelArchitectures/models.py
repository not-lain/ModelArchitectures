import torch.nn as nn

class Model1(nn.Module):
    def __init__(self,a,b):
        super().__init__()
        self.layer = nn.Linear(a,b)
    def forward(self,data):
        return self.layer(data)
    
class Model2(nn.Module): 
    def __init__(self, cfg):
        super().__init__()
        self.layer == nn.Linear(cfg.a,cfg.b)
    def forward(self, data): 
        super().__init__()
        return self.layer(data)

    
