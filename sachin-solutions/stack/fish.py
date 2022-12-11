def solution(fish_sizes, fish_directions):
    """Solution method implementation."""
    # stack and count initialization
    ds_fishes = []
    count = 0
    # iterate through the list of fishes:
    for i, _ in enumerate(fish_directions):
        # downstream fish
        if fish_directions[i]:
            ds_fishes.append(fish_sizes[i])
            continue
        # upstream fish - fighting all downstream stack
        while ds_fishes:
            # upstream fish loses and dies     
            if ds_fishes[-1] > fish_sizes[i]:
                break
            # upstream fish wins the match and fights another one       
            ds_fishes.pop()
        # loop didn't end prematurely = upstream fish ate the stack 
        else:
            count += 1
    # return upstream winners + remaining downstream fishes
    return count + len(ds_fishes)