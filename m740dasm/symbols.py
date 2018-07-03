from m740dasm.tables import AddressModes

class SymbolTable(object):
    def __init__(self, initial_symbols=None):
        if initial_symbols is None:
            initial_symbols = {}
        self.symbols = initial_symbols.copy()

    def generate(self, memory, start_address):
        self.generate_code_symbols(memory, start_address)
        #self.generate_data_symbols(memory, start_address)

    def generate_code_symbols(self, memory, start_address):
        for address in range(start_address, len(memory)):
            if address in self.symbols:
                pass # do not overwrite existing symbols
            elif memory.is_call_target(address):
                if memory.is_instruction_start(address):
                    self.symbols[address] = ('sub_%04x' % address, '')
            elif memory.is_jump_target(address):
                if memory.is_instruction_start(address):
                    self.symbols[address] = ('lab_%04x' % address, '')

    def generate_data_symbols(self, memory, start_address):
        # symbols are always generated for direct or extended address r/w
        for address, inst in memory.iter_instructions():
            if inst.addr_mode not in (AddressModes.Extended,
                                      AddressModes.Direct,
                                      AddressModes.DirectWithImmediateByte,
                                      AddressModes.BitDirect):
                continue
            if inst.address in self.symbols:
                continue
            if memory.is_single_byte_or_start_of_multibyte(inst.address):
                self.symbols[inst.address] = ('mem_%04x' % inst.address, '')

        # bbc 0xaa:0, 0xe005
        # symbols are always generated for the tested address (0xaa)
        for address, inst in memory.iter_instructions():
            if inst.addr_mode != AddressModes.BitDirectWithRelative:
                continue
            if inst.bittest_address in self.symbols:
                continue
            if memory.is_single_byte_or_start_of_multibyte(inst.bittest_address):
                self.symbols[inst.bittest_address] = ('mem_%04x' % inst.bittest_address, '')

        # mov ep, #0x0123
        # mov ix, #0x0123
        # mov sp, #0x0123
        # symbols are always generated for immediate words loaded into pointers
        for address, inst in memory.iter_instructions():
            if not inst.stores_immediate_word_in_pointer:
                continue
            if inst.immediate in self.symbols:
                continue
            if memory.is_single_byte_or_start_of_multibyte(inst.immediate):
                self.symbols[inst.immediate] = ('mem_%04x' % inst.immediate, '')

        # mov a, #0xee9f
        # symbols are only generated for immediate word loads into A if the
        # address is in the rom range or else many false positives will result
        for address, inst in memory.iter_instructions():
            if not inst.stores_immediate_word_in_a:
                continue
            if inst.immediate in self.symbols:
                continue
            if inst.immediate < start_address:
                continue
            if memory.is_single_byte_or_start_of_multibyte(inst.immediate):
                self.symbols[inst.immediate] = ('mem_%04x' % inst.immediate, '')


F2MC8L_COMMON_SYMBOLS = {
}

MB89620R_SYMBOLS = F2MC8L_COMMON_SYMBOLS.copy()
MB89620R_SYMBOLS.update({
})

MB89670_SYMBOLS = F2MC8L_COMMON_SYMBOLS.copy()
MB89670_SYMBOLS.update({
})
