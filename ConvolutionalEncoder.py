class ConvolutionalEncoder:
    _mappings = {
        "100": "11",
        "000": "00",
        "110": "00",
        "010": "11",
        "111": "10",
        "011": "01",
        "101": "01",
        "001": "10"
    }
    
    @staticmethod
    def encode(binary_string: str) -> str:
        result = ""
        shift_register = '00'
        for bit in binary_string:
            result += ConvolutionalEncoder._mappings[f'{bit}{shift_register}']
            shift_register = f'{bit}{shift_register[0]}'
        return result
