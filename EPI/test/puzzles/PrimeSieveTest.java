package puzzles;

import org.junit.Test;

import java.util.HashSet;
import java.util.Set;

public class PrimeSieveTest {

  @Test
  public void testGeneratePrimes() throws Exception {
    int N = 1000000;
    Set<Integer> primes = new HashSet<>(PrimeSieve.generatePrimes(N));
    for (int i = 0; i <= N; i++) {
      boolean expected = isPrime(i);
      boolean actual = primes.contains(i);
      assert expected == actual;
    }
  }

  private boolean isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i >= i && i * i <= n; i++) if (n % i == 0) return false;
    return true;
  }
}
