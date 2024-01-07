import struct
from rich import print
from numpy import float16, float32, float64, int16, uint16


def number_to_bytes(number):
    str_formats = {float64: 'd', float: 'd',
                   float32: 'f', float16: 'e',
                   int: 'i', int16: 'h', uint16: 'H'}
    formatter = str_formats[type(number)]
    bytes_str = ''
    packed_data = struct.pack(f'>{formatter}', number)
    for byte in packed_data:
        byte_str = format(byte, '08b')
        bytes_str += byte_str
    return bytes_str


def fractional_binary(binary: str) -> float:
    value = 1
    for position, byte in enumerate(binary):
        value += int(byte)*(2**(-position-1))
    return value


def preaty_print_float(number, exact_representation):
    # breakpoint()
    bytes_str = number_to_bytes(number)
    bits_info = {float16: (16, 5), float32: (
        32, 8), float64: (64, 11), float: (64, 11)}
    bits_total, bits_exp = bits_info[type(number)]
    bits_mantissa = bits_total-bits_exp-1
    sign_bit = bytes_str[0]
    exp_bias = 2**(bits_exp-1)-1
    exponent = int(bytes_str[1:bits_exp+1], 2)-exp_bias
    binary_exponent = bytes_str[1:bits_exp+1]
    mantissa = fractional_binary(bytes_str[bits_exp+1:])
    binary_mantissa = bytes_str[bits_exp+1:]
    print(f"{exact_representation} em representação Float{bits_total} =")
    print(f"[red]{sign_bit}[/red][green]{binary_exponent}[/green] \
          [bright_yellow]{binary_mantissa}[/bright_yellow]")
    print('')
    print(f"Sinal 1-bit: [red]{sign_bit}[/red] \
           {'(positivo)' if sign_bit else 'negativo'}")
    print('')
    print(f"Expoente {bits_exp}-bits: [green] \
          {binary_exponent}= {exponent+exp_bias}- \
          {exp_bias}=[/green]{exponent}")
    print('')
    print(f"Mantissa {bits_mantissa}-bits [bright_yellow] \
          {bytes_str[bits_exp+1:]}[/bright_yellow] = \
          {mantissa:.{bits_mantissa}f}")
    print("----------------")
    print(f"{exact_representation}(Float-{bits_total})=[bright_yellow]\
          {mantissa:.{bits_mantissa}f}[/bright_yellow]*(2^[green]{exponent}\
          [/green])={mantissa*2**exponent:.{bits_total}f}")


preaty_print_float(float32(4), '4')
