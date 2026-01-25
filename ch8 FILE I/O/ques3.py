def genrateTable(n):
    with open(f"tables/table_of_{n}.txt",'w') as f:
        for i in range(1,11):
            f.write(f"{n}*{i}={n*i}\n")
for i in range(2,21):
    genrateTable(i)
