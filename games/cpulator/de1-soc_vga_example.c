#define JTAG_UART_DATA ((volatile int*) 0xFF201000)
#define JTAG_UART_CONTROL ((volatile int*) (0xFF201000+4))
// 0xc9000000 for ARM; 0x09000000 for Nios, RISC-V
#define VGA_CHAR_BUFFER_ADDR 0xc9000000
// 0xc8000000 for ARM; 0x08000000 for Nios, RISC-V
#define VGA_PIX_BUFFER_ADDR 0xc8000000

/* set a single pixel on the screen at x,y
 * x in [0,319], y in [0,239], and color in [0,65535]
 */
void write_pixel(int x, int y, short color) {
    volatile short *vga_addr = (volatile short*)(VGA_PIX_BUFFER_ADDR + (y<<10) + (x<<1));
    *vga_addr = color;
}

/* write a single character to the character buffer at x,y
 * x in [0,79], y in [0,59]
 */
void write_char(int x, int y, char c) {
   // VGA character buffer
   volatile char * character_buffer = (char *) (VGA_CHAR_BUFFER_ADDR + (y<<7) + x);
   *character_buffer = c;
}

/* use write_pixel to set entire screen to black (does not clear the character buffer) */
void fill_screen(short color) {
    int x, y;
    for (x = 0; x < 320; x++) {
        for (y = 0; y < 240; y++) {
	        write_pixel(x, y, 0);
	    }
    }
}

void clear_char_buffer() {
    int x, y;
    for (x = 0; x < 80; x++) {
        for (y = 0; y < 60; y++) {
	        write_char(x, y, ' ');
	    }
    }
}

void main () {
    fill_screen(0);
    clear_char_buffer();

    char* str = "Hello World!";
    for (int i = 0; i < 12; i++) {
        write_char(i, 0, str[i]);
    }
}