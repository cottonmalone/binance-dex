import pytest
from binance.crypto import *


@pytest.mark.parametrize('phrase,key', [
    ("fragile duck lunch coyote cotton pole gym orange share muscle impulse "
     "mom pause isolate define oblige hungry sound stereo spider style river "
     "fun account",
     "caf2009a04bd53d426fc0907383b3f1dfe13013aee694d0159f6befc3fdccd5f"),
    ("offer caution gift cross surge pretty orange during eye soldier "
     "popular holiday mention east eight office fashion ill parrot "
     "vault rent devote earth cousin",
     "90335b9d2153ad1a9799a3ccc070bd64b4164e9642ee1dd48053c33f9a3a05e9")
])
def test_get_private_key_from_mnemonic(phrase, key):
    """
    Test function behaves as expected.
    """
    assert get_private_key_from_mnemonic(phrase) == key
