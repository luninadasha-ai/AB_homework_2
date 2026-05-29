import math

def calc_jc_transition(t, i, j):
    """Compute JC69 transition probability from state i to state j over time t."""
    if i == j:
        return 0.25 * (1 + 3 * math.exp(-4 * t / 3))
    else:
        return 0.25 * (1 - math.exp(-4 * t / 3))

def prob_of_tree(species_1, species_2, ancestor_3, t1, t2):
    prior_ancestor = 0.25  
    p_s1_given_anc = calc_jc_transition(t1, ancestor_3, species_1)
    p_s2_given_anc = calc_jc_transition(t2, ancestor_3, species_2)
    return prior_ancestor * p_s1_given_anc * p_s2_given_anc

def main():
    t1, t2 = 0.1, 0.1
    bases = ['A', 'C', 'G', 'T']
    print("For ancestor = G")
    p = prob_of_tree('A', 'A', 'G', t1, t2)
    print(f"P(1=A, 2=A, 3=G) = {p:.6f}")
    

    print("\nP(1=A, 2=A, 3=X) for all bases X")
    print(f"{'Ancestor X':<12} {'P(X)':<10} {'P(A|X,t1)':<14} {'P(A|X,t2)':<14} {'Joint P':<12}")
    
    results = {}
    for x in bases:
        joint = prob_of_tree('A', 'A', x, t1, t2)
        prior = 0.25
        p_s1 = calc_jc_transition(t1, x, 'A')
        p_s2 = calc_jc_transition(t2, x, 'A')
        results[x] = joint
        print(f"  {x:<12} {prior:<10.4f} {p_s1:<14.6f} {p_s2:<14.6f} {joint:<12.6f}")
    
    total = sum(results.values())
    print(f"\nTotal likelihood (sum over all X): {total:.6f}")

if __name__ == "__main__":
    main()