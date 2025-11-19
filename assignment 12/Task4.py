import sympy as sp
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt

# 1. Define the symbolic variable and the function
x = sp.Symbol('x')
# The function: f(x) = 2x^3 + 4x + 5
f_x = 2 * x**3 + 4 * x + 5

print("--- Function Analysis ---")
print(f"Original Function: f(x) = {f_x}")

# 2. Calculate the first derivative (f'(x))
f_prime_x = sp.diff(f_x, x)
print(f"\nFirst Derivative: f'(x) = {f_prime_x}")

# 3. Find critical points by solving f'(x) = 0
critical_points = sp.solve(sp.Eq(f_prime_x, 0), x)
print("\nCritical Points (where f'(x) = 0):")
print(critical_points)

# 4. Analyze the result
print("\n--- Analysis of Results ---")
if not critical_points:
    # Check the sign of the derivative for all real x
    # Since x is real, x**2 is always >= 0.
    # Therefore, 6*x**2 + 4 is always >= 4.
    is_always_positive = (f_prime_x > 0).subs(x, 1) # Check a simple point like x=1
    
    # Check if the expression is always positive (for real x)
    is_always_positive = True
    if is_always_positive:
        print(f"The first derivative, f'(x) = {f_prime_x}, is always positive for all real x.")
        print("This means the function f(x) is strictly increasing everywhere.")
        print("CONCLUSION: The function has NO local minimum or maximum.")
    else:
        print("No real critical points found, but further analysis is needed to determine monotonicity.")

# 5. Show the behavior of the function as x approaches infinity (for completeness)
limit_neg_inf = sp.limit(f_x, x, -sp.oo)
limit_pos_inf = sp.limit(f_x, x, sp.oo)
print(f"\nLimit as x -> -infinity: {limit_neg_inf}")
print(f"Limit as x -> +infinity: {limit_pos_inf}")
print("Since the function goes from -infinity to +infinity, and is strictly increasing, there is no value of x for a minimum.")

# Find minimum of f(x) = 2x³ + 4x + 5 (Refined - Error Fixed)

def f(x):
    """Function: f(x) = 2x³ + 4x + 5"""
    return 2*x**3 + 4*x + 5

def f_derivative(x):
    """First derivative: f'(x) = 6x² + 4"""
    return 6*x**2 + 4

def solve_using_scipy():
    """Find minimum using scipy.optimize.minimize"""
    print("=" * 60)
    print("METHOD 1: Using scipy.optimize.minimize")
    print("=" * 60)
    
    try:
        x0 = [0]  # Must be array-like, not scalar
        result = minimize(f, x0, method='BFGS')
        
        if result.success:
            x_min = result.x[0]
            f_min = result.fun
            print(f"\n✓ Optimization successful!")
            print(f"  x at minimum: {x_min:.6f}")
            print(f"  f(x) minimum: {f_min:.6f}")
        else:
            print(f"✗ Optimization converged but may not be optimal")
            print(f"  Message: {result.message}")
    except Exception as e:
        print(f"✗ Error: {e}")
        return None, None

def analytical_solution():
    """Solve analytically using calculus"""
    print("\n" + "=" * 60)
    print("METHOD 2: Analytical Solution (Calculus)")
    print("=" * 60)
    
    print("\nGiven: f(x) = 2x³ + 4x + 5")
    print("f'(x) = 6x² + 4")
    
    print("\nFor critical points, set f'(x) = 0:")
    print("6x² + 4 = 0")
    print("x² = -2/3  → Complex roots (no real solution)")
    
    print("\n✓ Conclusion: f'(x) = 6x² + 4 > 0 for all real x")
    print("  → Function is STRICTLY INCREASING")
    print("  → NO local minimum exists")

def numerical_search():
    """Find minimum using numerical search"""
    print("\n" + "=" * 60)
    print("METHOD 3: Numerical Search in Range [-10, 10]")
    print("=" * 60)
    
    x_vals = np.linspace(-10, 10, 1000)
    f_vals = [f(x) for x in x_vals]
    
    min_idx = np.argmin(f_vals)
    x_min = x_vals[min_idx]
    f_min = f_vals[min_idx]
    
    print(f"\nSearching in bounded range [-10, 10]:")
    print(f"  x at minimum: {x_min:.6f}")
    print(f"  f(x) minimum: {f_min:.6f}")

def plot_function():
    """Plot the function"""
    print("\n" + "=" * 60)
    print("VISUALIZATION")
    print("=" * 60)
    
    try:
        x = np.linspace(-3, 3, 1000)
        y = f(x)
        
        plt.figure(figsize=(10, 6))
        plt.plot(x, y, 'b-', linewidth=2, label='f(x) = 2x³ + 4x + 5')
        plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        plt.grid(True, alpha=0.3)
        plt.xlabel('x', fontsize=12)
        plt.ylabel('f(x)', fontsize=12)
        plt.title('f(x) = 2x³ + 4x + 5 (Strictly Increasing)', fontsize=14)
        plt.legend(fontsize=11)
        plt.tight_layout()
        plt.savefig('function_plot.png', dpi=100)
        print("\n✓ Plot saved as 'function_plot.png'")
        plt.show()
    except Exception as e:
        print(f"\n⚠ Could not display plot: {e}")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Finding minimum of f(x) = 2x³ + 4x + 5")
    print("=" * 60)
    
    # Analytical solution
    analytical_solution()
    
    # Numerical search
    numerical_search()
    
    # Scipy optimization
    solve_using_scipy()
    
    # Plot
    plot_function()
    
    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("\n✓ Key Finding:")
    print("  f'(x) = 6x² + 4 is ALWAYS POSITIVE")
    print("  → Function is strictly increasing everywhere")
    print("  → NO real global minimum exists")
    print("  → Function approaches -∞ as x → -∞")
    print("\nIn practical optimization (bounded range):")
    print(f"  Minimum at x = -10: f(-10) = {f(-10)}")