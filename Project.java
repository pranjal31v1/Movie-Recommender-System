import java.util.*;

public class Project {
    public static void main(String[] args) throws Exception {
        if (args.length > 0) {
            List<String> genres = GenreUtils.parseGenres(args[0]);
            List<Map<String, Integer>> result = GenreUtils.encodeGenres(genres);
            for (int i = 0; i < Math.min(result.size(), 5); i++) {
                System.out.println(result.get(i));
            }
        }
    }
}
