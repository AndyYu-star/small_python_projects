import random

def hypervolume(d,SAMPLES):
    hits = 0
    for i in range(SAMPLES):
        total = 0
        for i in range(d):
            n = random.uniform(-1,1)
            total += n**2
            if total >= 1:
                break
        if total < 1:
            hits += 1
    return (hits/SAMPLES)*(2**d)

print("Volumes:")
for d in range(2,21):
    print("Dimension " + str(d) + ": " + str(hypervolume(d,1000000)))


def hypersurface(d,SAMPLES):
    RESOLUTION = 0.01
    hits = 0
    for i in range(SAMPLES):
        total = 0
        for i in range(d):
            n = random.uniform(0,1)
            total += n**2
            if total >= 1+RESOLUTION:
                break
        if abs(total - 1) < RESOLUTION:
            hits += 1
    return (hits/SAMPLES)*(2**d)/RESOLUTION

print("Surface areas:")
for d in range(2,21):
    print("Dimension " + str(d) + ": " + str(hypersurface(d,1000000)))
