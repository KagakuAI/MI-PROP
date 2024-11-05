from miprop.mil.network.module.attention import AttentionNetwork, SelfAttentionNetwork, GatedAttentionNetwork, \
    TemperatureAttentionNetwork, GlobalTemperatureAttentionNetwork, GumbelAttentionNetwork
from miprop.mil.network.module.base import BaseClassifier
from miprop.mil.network.module.dynamic import DynamicPoolingNetwork, MarginLoss
from miprop.mil.network.module.gaussian import GaussianPoolingNetwork
from miprop.mil.network.module.hopfield import HopfieldNetwork
from miprop.mil.network.module.classic import BagNetwork, InstanceNetwork


class AttentionNetworkClassifier(AttentionNetwork, BaseClassifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class SelfAttentionNetworkClassifier(SelfAttentionNetwork, BaseClassifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GatedAttentionNetworkClassifier(GatedAttentionNetwork, BaseClassifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class TemperatureAttentionNetworkClassifier(TemperatureAttentionNetwork, BaseClassifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GlobalTemperatureAttentionNetworkClassifier(GlobalTemperatureAttentionNetwork, BaseClassifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GumbelAttentionNetworkClassifier(GumbelAttentionNetwork, BaseClassifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BagNetworkClassifier(BagNetwork, BaseClassifier):

    def __init__(self, pool='mean', **kwargs):
        super().__init__(pool=pool, **kwargs)


class InstanceNetworkClassifier(InstanceNetwork, BaseClassifier):
    def __init__(self, pool='mean', **kwargs):
        super().__init__(pool=pool, **kwargs)


class GaussianPoolingNetworkClassifier(GaussianPoolingNetwork, BaseClassifier):
    def __init__(self, pool='lse', **kwargs):
        super().__init__(pool=pool, **kwargs)


class DynamicPoolingNetworkClassifier(DynamicPoolingNetwork, BaseClassifier):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def loss(self, y_pred, y_true):
        margin_loss = MarginLoss()
        loss = margin_loss(y_pred, y_true.reshape(-1, 1))
        return loss
