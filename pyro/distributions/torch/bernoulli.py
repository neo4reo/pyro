from __future__ import absolute_import, division, print_function

import torch

from pyro.distributions.bernoulli import Bernoulli as _Bernoulli
from pyro.distributions.torch_wrapper import TorchDistribution
from pyro.distributions.util import copy_docs_from


@copy_docs_from(_Bernoulli)
class Bernoulli(TorchDistribution):
    enumerable = True

    def __init__(self, ps=None, logits=None, *args, **kwargs):
        torch_dist = torch.distributions.Bernoulli(probs=ps, logits=logits)
        x_shape = logits.shape if ps is None else ps.shape
        event_dim = 1
        super(Bernoulli, self).__init__(torch_dist, x_shape, event_dim, *args, **kwargs)

    def sample(self):
        return super(Bernoulli, self).sample().type_as(self.torch_dist.probs)

    def batch_log_pdf(self, x):
        return super(Bernoulli, self).batch_log_pdf(x.long())

    def enumerate_support(self):
        return super(Bernoulli, self).enumerate_support().type_as(self.torch_dist.probs)
