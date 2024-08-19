import random

def getInputs():
    num_flips = int(input("Enter the number of times to flip the coin: "))
    return num_flips

def simulateFlips(num_flips):
    heads_count = 0
    tails_count = 0
    
    for _ in range(num_flips):
        if random.random() < 0.5:
            heads_count += 1
        else:
            tails_count += 1
    
    return heads_count, tails_count

def displayResults(heads_count, tails_count):
    total_flips = heads_count + tails_count
    heads_proportion = heads_count / total_flips
    tails_proportion = tails_count / total_flips
    
    print(f"Heads {heads_proportion:.2f}, Tails {tails_proportion:.2f}")

def main():
    num_flips = getInputs()
    heads_count, tails_count = simulateFlips(num_flips)
    displayResults(heads_count, tails_count)

if __name__ == "__main__":
    main()