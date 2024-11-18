# Solving the Travelling Salesman Problem: A Numerical Approach

### Authors
Juan Jose Velez Orozco, David Naranjo Lopez  

**Date:** _`18/11/2024`_  
**Institution:** Universidad EAFIT  

---

## Introduction

The traveling salesman problem is a classic problem in optimization and combinatorial mathematics. It involves a salesman who is given a set of cities, and the task is to find the shortest possible route that visits each city exactly once and returns to the starting point. The problem is NP-hard, meaning that no polynomial algorithm is known to solve it for large data sets.

There are several approaches to solving the TSP, including exact algorithms and heuristic methods. Some of the most commonly used algorithms for solving the TSP are:

---

## Algorithms

### Brute Force Algorithm
This method consists of calculating all possible routes and selecting the one with the shortest distance. Although this method guarantees the correct solution, it is computationally expensive. The number of possible routes grows factorially with the number of cities, making it impractical for large data sets. This method has a time complexity of \(O(n!)\), where \(n\) is the number of cities.

### Nearest Neighbor Algorithm
This is a simple heuristic method for solving the TSP. It starts by selecting a city at random and then repeatedly chooses the nearest unvisited city as the next destination. This process continues until all cities have been visited. Although this method is faster, it does not always produce the optimal solution. Its time complexity is \(O(n^2)\).

### Simulated Annealing
Inspired by the annealing process in metallurgy, this algorithm starts with a random solution and iteratively makes small changes. The algorithm accepts worse solutions with some probability to avoid getting stuck in local minima. Its time complexity is \(O(n^2)\).

### Ant Colony Optimization
Ants deposit pheromones on the paths they travel, which influences the probability that other ants will choose the same path. The algorithm uses this mechanism to search for the shortest path. Over time, the pheromone trails evaporate, encouraging exploration of new paths. ACO is especially effective for large TSP cases and has a time complexity of \(O(n^2)\), though it depends on the implementation and parameters.

### Genetic Algorithm
GAs generate a population of candidate solutions and evolve them over several generations. The algorithm uses crossover (recombination) and mutation operators to produce new solutions. GAs can provide good approximations to the optimal solution, although they do not guarantee the best result. Time complexity is \(O(n^2)\) in many cases, depending on the implementation and population size.

---

## Selected Algorithm: Simulated Annealing

For this project, we selected the Simulated Annealing algorithm. This choice was based on its trade-off between computational efficiency and solution quality. Among the algorithms considered, Simulated Annealing proved to be one of the most efficient in a limited time frame. Although other methods, such as ant colony optimization and genetic algorithms, can achieve superior results, they tend to require much more time to converge, making them less practical for this competition.

We experimented with the application of Simulated Annealing in three different programming languages: Python, C++, and Java. Both C++ and Java demonstrated superior performance in terms of speed of execution and quality of solutions, with Java ultimately being chosen for its ease of implementation and scalability.

To further optimize performance, we attempted to parallelize the algorithm to take better advantage of CPU capabilities. However, this approach did not yield significant improvements in execution time or solution quality.

For comparison, we also experimented with the brute force algorithm. As expected, it was computationally infeasible for large data sets due to its factorial complexity.

---

## Pseudocode: Simulated Annealing

The following pseudocode outlines the steps for the Simulated Annealing algorithm used to solve the Travelling Salesman Problem:

1. **Input:** `Distance`, `InitialTemperature`, `CoolingRate`, `Iterations`.
2. **Output:** `BestRoute` (array), `BestLength` (float).
3. Initialize `CurrentRoute` as a sequence of all cities.
4. Shuffle `CurrentRoute` randomly.
5. Set `BestRoute = CurrentRoute`.
6. Calculate `BestLength` = Length of `BestRoute` using `DistanceMatrix`.
7. Set `Temperature = InitialTemperature`.
8. **While** `Temperature > 1`:
    - **For** i = 1 to `Iterations`:
        1. Generate `NewRoute`:
            - Clone `CurrentRoute`.
            - Select two random indices (`Index1`, `Index2`).
            - Reverse the subarray between `Index1` and `Index2` in `NewRoute`.
        2. Calculate `NewLength` = Length of `NewRoute`.
        3. Set `Delta` = `NewLength` - Length of `CurrentRoute`.
        4. **If** `Delta < 0` **or** `Random(0, 1) < e^(-Delta / Temperature)`:
            - Set `CurrentRoute = NewRoute`.
            - **If** `NewLength < BestLength`:
                - Set `BestRoute = NewRoute`.
                - Set `BestLength = NewLength`.
    - Decrease `Temperature` = `Temperature * CoolingRate`.
9. **Return:** `BestRoute`, `BestLength`.

---

## Conclusion

The *Simulated Annealing* algorithm has proven to be a valuable tool for tackling complex optimization problems such as the TSP due to its balance between simplicity, efficiency, and its ability to find high-quality solutions. Although it does not guarantee the optimal result, its design allows escaping local minima, achieving near-optimal solutions within reasonable computational times.

Choosing Simulated Annealing over other methods, such as brute force or genetic algorithms, is justified by its lower computational cost and adaptability to the problem. This approach is particularly useful as the number of cities increases, where other exact techniques become impractical.

In the implementation presented:  
- **Results:** Routes were significantly optimized within a limited number of iterations.  
- **Impact:** Its ease of implementation and ability to adjust parameters make it ideal for scenarios with constrained time and resources.  

As future work, exploring its combination with other heuristic methods, such as particle swarm optimization, or parallelizing its execution to better leverage available hardware, could be considered. This would allow obtaining faster and more robust solutions, maximizing the algorithm's potential for real-world applications.



---

## References

1. [WS Cube Tech - Travelling Salesman Problem](https://www.wscubetech.com/resources/dsa/travelling-salesman-problem)
2. [John Walker - Simulated Annealing for the Travelling Salesman Problem](https://www.fourmilab.ch/documents/travelling/anneal/)
3. [David Liang - Intro Python Algorithms: Traveling Salesman Problem](https://medium.com/@davidlfliang/intro-python-algorithms-traveling-salesman-problem-ffa61f0bd47b)
4. [GeeksforGeeks - Travelling Salesman Problem using Dynamic Programming](https://www.geeksforgeeks.org/travelling-salesman-problem-using-dynamic-programming/)
5. [Wikipedia - Problema del viajante](https://es.wikipedia.org/wiki/Problema_del_viajante)
6. [Baobab Soluciones - Problema del viajante](https://baobabsoluciones.es/blog/2020/10/01/problema-del-viajante/)
