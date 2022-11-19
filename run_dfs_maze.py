from PIL import Image
import sys
sys.setrecursionlimit(15000)
im = Image.open("maze_bfs.png")
print(im.format, im.size, im.mode)

pixels = im.load()

rdim, cdim = im.size

red = (255,0,0, 255)
blue = (0,0,255, 255)
white = (255,255,255, 255)
black = (0,0,0, 255)

def run_dfs(pixels,curr,visited):
    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        visited.add(curr)
        new = curr[0] + dr, curr[1] + dc
        if new[0] < rdim and new[1] < cdim and new[0]  >= 0 and new[1] >= 0:
            if pixels[new[0],new[1]] == red:
                return (curr,new)
            elif pixels[new[0],new[1]] == white:
                if new not in visited:
                    res = run_dfs(pixels, new, visited)
                    if res is not None:
                        return (curr,)+res
                    else:
                        visited.remove(curr)
    return None

pos = run_dfs(pixels,(0,1),set())

for r,c in pos:
    pixels[r,c] = blue

# im.show()


im.save("dfs_out.png")
