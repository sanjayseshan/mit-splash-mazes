from PIL import Image

# im = Image.open("maze_bfs.png")
im = Image.open("large_maze.png")
print(im.format, im.size, im.mode)

pixels = im.load()

rdim, cdim = im.size

red = (255,0,0, 255)
blue = (0,0,255, 255)
white = (255,255,255, 255)
black = (0,0,0, 255)

def run_bfs(pixels,rdim, cdim):
    Q = [((0,1),)]
    while Q != []:
        path = Q.pop(0)
        curr = path[-1]
        for dr, dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            new = curr[0] + dr, curr[1] + dc
            if  new[0] < rdim and new[1] < cdim and new[0]  >= 0 and new[1] >= 0:
                if pixels[new[0],new[1]] == red:
                    return path+(new,)
                elif pixels[new[0],new[1]] == white:
                    if new not in path:
                        new_path = path+(new,)
                        Q.append(new_path)
    return None

pos = run_bfs(pixels,rdim,cdim)

for r,c in pos:
    pixels[r,c] = blue

# im.show()

im.save("bfs_out_lg.png")