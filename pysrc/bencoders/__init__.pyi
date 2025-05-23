_BencodeBases = bytes | int
Bencode = _BencodeBases | list[_BencodeBases] | dict[bytes, _BencodeBases]

class Bencoder:
    def __new__(cls) -> Bencoder: ...
    def parse(self, data: bytes) -> Bencode: ...
