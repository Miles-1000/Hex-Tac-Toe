def f(x):
    r = 1.4
    return (r**(x+1)-1)/(r-1)

# def norm_val(x):
#     return int((f(x) / (6 * f(5))) * 100)

# for a in range(1179, 1579):
#     r = a/1000

#     vals = [0,
#     (2 * f(2)),
#     f(4),
#     (2 * f(4)),
#     (6 * f(2)),
#     f(5),
#     (6 * f(5))]

#     result = ""

#     for i in range(len(vals)-1):
#         cond = vals[i]<vals[i+1]
#         result += "Y" if cond else "N"

    
#     print(f"{r:.3f}: {result}")

#     if result.count("N") == 0:
#         break

# for i in range(1,7):
#     print(f"{i}: {norm_val(i)}")


vals = [0,
(2 * f(2)),
f(4),
(2 * f(4)),
(6 * f(2)),
f(5),
(6 * f(5))]

result = ""

for i in range(len(vals)-1):
    cond = vals[i]<vals[i+1]
    result += "Y" if cond else "N"

print(result)