import java.io.FileReader;
import java.io.FileWriter;

import java.util.List;
import java.util.ArrayList;

import org.topcoder.TopcoderReader;
import org.topcoder.TopcoderWriter;
import org.topcoder.TypeRef;

public class ShopPositionsSolver {
    public static void main(String[] args) {
    try {
        TopcoderReader reader = new TopcoderReader(new FileReader(args[0]));
        int n = (Integer) reader.next(Integer.class);
        reader.next();
        
        int m = (Integer) reader.next(Integer.class);
        reader.next();
        
        List<Integer> cBoxed = (List<Integer>) reader.next(new TypeRef<List<Integer>>(){}.getType());
        int[] c = new int[cBoxed.size()];
        for (int _i = 0; _i < cBoxed.size(); ++_i)
            c[_i] = cBoxed.get(_i);
        reader.close();

        ShopPositions solver = new ShopPositions();
        TopcoderWriter writer = new TopcoderWriter(new FileWriter(args[1]));
        writer.write(solver.maxProfit(n, m, c));
        writer.close();
    } catch (Exception err) {
        err.printStackTrace(System.err);
    }
    }
}
