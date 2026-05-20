"""
JSSIM Night 1: Coin Flip Monte Carlo
Goal: Understand Expected Value and Variance
"""
import random

def run_simulation(num_flips):
    pnl = 0
    results = []
    
    for i in range(num_flips):
        # +1 for heads, -1 for tails
        flip = random.choice([1, -1])
        pnl += flip
        results.append(pnl)
    
    return pnl, results

if __name__ == "__main__":
    NUM_FLIPS = 1000
    final_pnl, history = run_simulation(NUM_FLIPS)
    
    print(f"=== JSSIM Night 1 Results ===")
    print(f"Total flips: {NUM_FLIPS}")
    print(f"Final PnL: ${final_pnl}")
    print(f"Expected Value: $0")
    print(f"Actual vs EV: ${final_pnl}")
    print(f"")
    print(f"Why not zero? Variance. Run it again, get different number.")
    print(f"Next: Night 2 we add bid/ask spread.")
