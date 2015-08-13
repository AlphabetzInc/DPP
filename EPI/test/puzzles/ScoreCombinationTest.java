package puzzles;

import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

public class ScoreCombinationTest {
    @Test
    public void testBookExample() {
        int s = 12;
        List<Integer> W = new ArrayList<Integer>();
        W.add(2);
        W.add(3);
        W.add(7);

        assert (4 == ScoreCombination.countCombinationsRecursive(s, W));
        assert (4 == ScoreCombination.countCombinationsDP(s, W));

        assert (18 == ScoreCombination.countPermutationsRecursive(s, W));
        assert (18 == ScoreCombination.countPermutationsDP(s, W));
    }

}