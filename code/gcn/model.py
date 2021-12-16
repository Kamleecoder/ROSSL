import  torch
from    torch import nn
from    torch.nn import functional as F
from    code.gcn.layer import GraphConvolution

from    code.gcn.config import args

class GCN(nn.Module):


    def __init__(self, input_dim, output_dim, num_features_nonzero=False):
        super(GCN, self).__init__()

        self.input_dim = input_dim #
        self.output_dim = output_dim

        print('input dim:', input_dim)
        print('output dim:', output_dim)
        print('num_features_nonzero:', num_features_nonzero)


        self.layers = nn.Sequential(
                                    GraphConvolution(self.input_dim, output_dim, num_features_nonzero,
                                                     activation=F.relu,
                                                     dropout=args.dropout,
                                                     is_sparse_inputs=False if not num_features_nonzero else True),
                                    )

    def forward(self, inputs):
        x, support = inputs

        x = self.layers((x, support))

        return x

    def l2_loss(self):

        layer = self.layers.children()
        layer = next(iter(layer))

        loss = None

        for p in layer.parameters():
            if loss is None:
                loss = p.pow(2).sum()
            else:
                loss += p.pow(2).sum()

        return loss
