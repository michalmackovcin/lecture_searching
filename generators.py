from random import choices


def unordered_sequence(max_len=100):
    """
    Generates a list of random integers in arbitrary order.

    Args:
        max_len (int): Desired length of the sequence.

    Returns:
        list[int]: List of randomly selected integers from range -1000 to 999.
    """
    return choices(range(-1000, 1000), k=max_len)


def ordered_sequence(max_len=100):
    """
    Generates a sorted list of random integers.

    Args:
        max_len (int): Desired length of the sequence.

    Returns:
        list[int]: Sorted list of randomly selected integers
        from range -1000 to 999.
    """
    return sorted(choices(range(-1000, 1000), k=max_len))


def dna_sequence(max_len=100):
    """
    Generates a random DNA sequence.

    Args:
        max_len (int): Desired length of the sequence.

    Returns:
        str: String composed of characters "A", "C", "G", "T".
    """
    return "".join(choices("ACGT", k=max_len))


def main():
    """
    Runs basic tests for sequence generation functions.
    """
    print(unordered_sequence(max_len=500))
    print(ordered_sequence(max_len=500))
    print(dna_sequence(max_len=500))


if __name__ == "__main__":
    main()
import random
import time

def linear_search(zoznam, hladane):
    pozícia= []
    počet= 0
    i= 0
    while i < len(zoznam):
        if zoznam[i]==hladane:
            pozícia.append(i)
            počet +=1
        i +=1
    return {
        "positions":pozícia,
        "count":počet
    }

def binary_search(list,chcené):
    lavy=0
    pravy=len(list)
    while lavy <= pravy:
        stred=(lavy+pravy)//2

        if list[stred]==chcené:
            return stred
        elif list[stred] < chcené:
            lavy=stred+1
        else:
            pravy=stred-1
    return None
def generuj_sekvenciu(dlzka, max_hodnota=1000):
    """Vytvorí zoznam náhodných celých čísel danej dĺžky."""
    return [random.randint(0, max_hodnota) for _ in range(dlzka)]
def meraj_cas(funkcia, *args):
    start = time.time()
    funkcia(*args)
    end = time.time()
    return end - start

def main():
    velkosti = [100, 500, 1000, 5000, 10000]
    cas_linear = []
    cas_binary = []

    for n in velkosti:
        subor = generuj_sekvenciu(n)
        subor_sorted = sorted(subor)
        hladane = subor[n // 2]

        # linear search
        t_linear = meraj_cas(linear_search, subor, hladane)
        cas_linear.append(t_linear)
        print(f"Linear search, n={n}: {t_linear:.6f} s")

        # binary search
        t_binary = meraj_cas(binary_search, subor_sorted, hladane)
        cas_binary.append(t_binary)
        print(f"Binary search, n={n}: {t_binary:.6f} s")


if __name__ == "__main__":
    main()


