def dfs(self, image: List[List[int]], sr: int, sc: int, color: int, val: int):
    if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] == color or image[sr][sc] != val:
        return None
    image[sr][sc] = color
    self.dfs(image, sr+1, sc, color, val)
    self.dfs(image, sr-1, sc, color, val)
    self.dfs(image, sr, sc+1, color, val)
    self.dfs(image, sr, sc-1, color, val)

def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    temp = image[sr][sc]
    self.dfs(image, sr, sc, color, temp)
    return image