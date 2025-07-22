import java.io.*;
import java.nio.file.*;
import java.util.*;

public class Project {
    public static final List<String> GENRES = Arrays.asList(
        "Action",
        "Comedy",
        "Sci-Fi",
        "Adventure",
        "Drama",
        "Horror",
        "Thriller",
        "Animation",
        "Romance",
        "Fantasy",
        "Family",
        "History",
        "Biography",
        "Music",
        "Mystery",
        "Crime"
    );

    public static List<Map<String, Integer>> encodeGenres(List<String> genreStrings) {
        List<Map<String, Integer>> encoded = new ArrayList<>();
        for (String gstr : genreStrings) {
            Map<String, Integer> row = new LinkedHashMap<>();
            for (String g : GENRES) {
                row.put(g, gstr != null && gstr.contains(g) ? 1 : 0);
            }
            encoded.add(row);
        }
        return encoded;
    }

    public static List<String> parseGenres(String csvPath) throws IOException {
        List<String> genres = new ArrayList<>();
        try (BufferedReader br = Files.newBufferedReader(Paths.get(csvPath))) {
            String header = br.readLine();
            if (header == null) {
                return genres;
            }
            String[] headers = header.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)");
            int genreIndex = -1;
            for (int i = 0; i < headers.length; i++) {
                if ("Genre".equals(headers[i])) {
                    genreIndex = i;
                    break;
                }
            }
            if (genreIndex == -1) {
                return genres;
            }
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)");
                if (genreIndex < parts.length) {
                    String genre = parts[genreIndex];
                    if (genre.startsWith("\"") && genre.endsWith("\"")) {
                        genre = genre.substring(1, genre.length() - 1);
                    }
                    genres.add(genre);
                }
            }
        }
        return genres;
    }

    public static void main(String[] args) throws Exception {
        if (args.length > 0) {
            List<String> genres = parseGenres(args[0]);
            List<Map<String, Integer>> result = encodeGenres(genres);
            for (int i = 0; i < Math.min(result.size(), 5); i++) {
                System.out.println(result.get(i));
            }
        }
    }
}
