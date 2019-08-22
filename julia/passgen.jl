using Nettle

pass = 0

function input(prompt::AbstractString = "")
	print(prompt * " ")
	chomp(readline())
end

function ask_pass()
	global pass = 1
	global hash = input("Enter Windows Hash: ")
end

function ntlm_hash()
if pass != 1
	count = 0
	ask_pass()
else
	h = Hasher("MD4")
	update!(h, z_set)
	h = hexdigest!(h)
	if hash == h
		println("\n")
		println(z_set, ":", h)
		exit()
	else
		println(z_set, ":", h)
	end
end
end

function gen_perm()
	i = 0
	for p in permutations(split(z_set, ""))
		print(join(p), "\n")
		i += 1
		i %= 12
		i != 0
	end
end

function gen_pass()
	v = ARGS[2]
	global z = length(c_set)
	f_set = Any[]
	while length(f_set) != parse(Int, v)
		for i in rand(1:z)
			for x in c_set[i]
				push!(f_set, x)
			end
		end
	end
global z_set = join(f_set)
if ARGS[3] == "-ntlm"
	ntlm_hash()
elseif ARGS[3] == "-norm"
	println(z_set)
elseif ARGS[3] == "-perm"
	gen_perm()
else
	println("Refer to argument switches")
end
end

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
b32 = ['2', '3', '4', '5', '6', '7']

while true
	if ARGS[1] == "-l"
		global c_set = lower
		gen_pass()
	elseif ARGS[1] == "-u"
		global c_set = upper
		gen_pass()
	elseif ARGS[1] == "-lu"
		global c_set = vcat(lower, upper)
		gen_pass()
	elseif ARGS[1] == "-n"
		global c_set = num
		gen_pass()
	elseif ARGS[1] == "-ln"
		global c_set = vcat(lower, num)
		gen_pass()
	elseif ARGS[1] == "-un"
		global c_set = vcat(upper, num)
		gen_pass()
	elseif ARGS[1] == "-lun"
		global c_set = vcat(lower, upper, num)
		gen_pass()
	elseif ARGS[1] == "-b32"
		global c_set = vcat(lower, b32)
		gen_pass()
	else
		println("Arguments: -l [num] -norm")
		break
	end
end
