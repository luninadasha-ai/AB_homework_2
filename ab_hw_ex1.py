def row_sums(dist):
    """Return r_i for every current taxon/cluster."""
    return {i: sum(dist[i][j] for j in dist if j != i) for i in dist}


def nj_R_matrix(dist):
    """Return the NJ R-matrix as a nested dictionary."""
    n = len(dist)
    r = row_sums(dist)
    R = {}
    for i in dist:
        R[i] = {}
        for j in dist:
            if i == j:
                R[i][j] = 0
            else:
                R[i][j] = (n - 2) * dist[i][j] - r[i] - r[j]
    return R


def nj_first_join(dist):
    """Return the pair with the smallest R-value."""
    R = nj_R_matrix(dist)
    best_pair = None
    best_val = 1000000
    for i in R:
        for j in R[i]:
            if i != j:
                if R[i][j] < best_val:
                    best_val = R[i][j]
                    best_pair = (i, j)
    return best_pair

def main():
    dist = {
        "Human": {"Human": 0, "Chimpanzee": 8.8,  "Gorilla": 10.3, "Orangutan": 16.1, "Gibbon": 18.1},
        "Chimpanzee": {"Human": 8.8,  "Chimpanzee": 0, "Gorilla": 10.6, "Orangutan": 17.2, "Gibbon": 18.9},
        "Gorilla": {"Human": 10.3, "Chimpanzee": 10.6, "Gorilla": 0,  "Orangutan": 16.7, "Gibbon": 18.9},
        "Orangutan": {"Human": 16.1, "Chimpanzee": 17.2, "Gorilla": 16.7, "Orangutan": 0,  "Gibbon": 18.9},
        "Gibbon": {"Human": 18.1, "Chimpanzee": 18.9, "Gorilla": 18.9, "Orangutan": 18.9, "Gibbon": 0},
    }

    print("Row sums")
    r = row_sums(dist)
    for species, val in r.items():
        print(f"r_{species} = {val}")

    print("\nR matrix")
    R = nj_R_matrix(dist)
    species = list(dist.keys())
    header = f"{'':12}" + "".join(f"{s:12}" for s in species)
    print(header)
    for i in species:
        row = f"{i:12}" + "".join(f"{R[i][j]:12.1f}" for j in species)
        print(row)
    
    print("\nAll pairwise R values:")
    print()

    pairs = []
    for i in species:
        for j in species:
            if j > i:
                pairs.append((i, j, dist[i][j], r[i], r[j], R[i][j]))

    pairs.sort(key=lambda x: x[5])

    for i, j, dij, ri, rj, rij in pairs:
        print(f"{i+' + '+j:<30} {dij:>8.1f}  {ri:>8.1f}  {rj:>8.1f}  {rij:>8.1f}")


    print("\nFirst NJ join")
    pair = nj_first_join(dist)
    best_R = R[pair[0]][pair[1]]
    print(f"Best pair: {pair[0]} + {pair[1]}")
    print(f"R value: {best_R:.1f}")


if __name__ == "__main__":
    main()
