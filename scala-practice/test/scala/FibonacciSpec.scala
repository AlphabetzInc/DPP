package scala

import org.scalacheck.Gen
import org.scalatest.FlatSpec
import org.scalatest.prop.GeneratorDrivenPropertyChecks._

/**
  * Created by pankaj on 6/21/16.
  */
class FibonacciSpec extends FlatSpec {

  val gen = Gen.choose[Int](2, 100000)

  "Sum of F(n) + F(n + 1)" should "equal F(n + 2)" in {
    forAll(gen) { (n) =>
      assertResult(TailRecursiveFibonacci(n)) {
        TailRecursiveFibonacci(n - 1) + TailRecursiveFibonacci(n - 2)
      }
      assertResult(IterativeFibonacci(n)) {
        IterativeFibonacci(n - 1) + IterativeFibonacci(n - 2)
      }
      assertResult(ClosedFormFibonacci(n)) {
        ClosedFormFibonacci(n - 1) + ClosedFormFibonacci(n - 2)
      }
      assertResult(MatrixFibonacci(n)) {
        MatrixFibonacci(n - 1) + MatrixFibonacci(n - 2)
      }
    }
  }

  "Nth Fibonacci number" should "match for all implementation" in {
    forAll(gen) { (n) =>
      val expected = IterativeFibonacci(n)
      assert(expected === TailRecursiveFibonacci(n))
      assert(expected === ClosedFormFibonacci(n))
      assert(expected - ClosedFormFibonacci1(n) <= 1)
      assert(expected === MatrixFibonacci(n))
    }
  }
}