import sys

class PageFrameTable:
    # Initialize the page frame table with the given number of frames (each frame is None)
    def __init__(self, num_frames):
        self.num_frames = num_frames
        self.page_frame_table = {i: None for i in range(num_frames)}
    # Return the physical frame number for the given page number (if it exists)
    def get_frame_num(self, page_num):
        if page_num in self.page_frame_table:
            return self.page_frame_table[page_num]
        else:
            return None
    # Handle a page fault by finding the first available frame and mapping the given page number to that frame
    def handle_page_error(self, page_num):
        for frame_num, page in self.page_frame_table.items():
            if page is None:
                self.page_frame_table[frame_num] = page_num
                return frame_num
        raise Exception("Page replacement not implemented")
    # Extract the page number from the given logical address (hexadecimal)
    def get_hex_address(hex_address):
        page_number = int(hex_address[:-2], 16)
        offset = int(hex_address[-2:], 16)
        return page_number, offset
if __name__ == "__main__":
    table = PageFrameTable(32)
    # Loop through the input addresses
    for input_hex in ["0x3A7F","0xABCD", "0x5678"]:
        # Extract the page number and offset from the given logical address
        page_num, offset = table.get_hex_address(input_hex)
        # Print the logical address, page number, and offset
        print(f"Logical Address: {input_hex} => Page Number: {page_num}, Offset: {offset:02X}")