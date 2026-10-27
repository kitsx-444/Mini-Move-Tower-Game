def move_target(n, source, target, spare):
	if n == 0:
		return
	move_target(n - 1, source, spare, target)
	print(f'Move disk {n} from {source} to {target}')
	move_target(n - 1, spare, target, source)


move_target(3, 'A', 'C', 'B')
