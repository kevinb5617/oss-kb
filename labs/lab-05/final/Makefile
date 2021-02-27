static:
	cc -c source/block.c -o source/block_static.o
	ar qc libblock.a source/block_static.o

shared:
	cc -fPIC -c source/block.c -o source/block_shared.o
	cc -shared -o libblock.so source/block_shared.o

make_static_block:
	cc -c program.c -o program.o
	cc program.o libblock.a -o static_block

make_dynamic_block:
	cc -c program.c -o program.o
	cc program.o libblock.so -o dynamic_block -Wl,-rpath .

