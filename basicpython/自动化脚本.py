import os

# 示例：批量重命名文件夹中的图片（先建一个测试目录再运行，避免 FileNotFoundError）
os.makedirs("photos", exist_ok=True)
for i in range(3):
    open(f"photos/old_{i}.jpg", "w").close()   # 创建 3 个空文件当示例

for i, filename in enumerate(os.listdir("photos/")):
    new_name = f"photo_{i+1}.jpg"
    os.rename(f"photos/{filename}", f"photos/{new_name}")

# 查看结果（实际项目中可删掉测试目录：os.removedirs 等）
print(os.listdir("photos/"))   # ['photo_1.jpg', 'photo_2.jpg', 'photo_3.jpg']