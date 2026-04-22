import java.sql.*;

public class LibraryManagement {
    public static void main(String[] args) {
        String url = "jdbc:mysql://localhost:3306/library_db";
        String user = "root";
        String password = "password";

        try (Connection conn = DriverManager.getConnection(url, user, password)) {

            // Issue a book (Update status to 'Issued' where id = 1)
            String issueQuery = "UPDATE Books SET status = 'Issued' WHERE id = ?";
            PreparedStatement pstmt = conn.prepareStatement(issueQuery);
            pstmt.setInt(1, 1);
            int rowsAffected = pstmt.executeUpdate();

            if(rowsAffected > 0) {
                System.out.println("Book Issued Successfully!");
            }

        } catch (SQLException e) {
            System.err.println("Database error occurred: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
