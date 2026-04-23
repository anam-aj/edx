// Interface defining a contract
interface Playable {
    // All methods in an interface are implicitly public and abstract (prior to Java 8)
    void play();
    void pause();
    void stop();
}

// Concrete class 1 implementing the interface
class AudioPlayer implements Playable {
    private String songTitle;

    public AudioPlayer(String songTitle) {
        this.songTitle = songTitle;
    }

    @Override
    public void play() {
        System.out.println("Playing audio: " + songTitle);
    }

    @Override
    public void pause() {
        System.out.println("Audio paused.");
    }

    @Override
    public void stop() {
        System.out.println("Audio stopped.");
    }
}

// Concrete class 2 implementing the interface
class VideoPlayer implements Playable {
    private String movieTitle;

    public VideoPlayer(String movieTitle) {
        this.movieTitle = movieTitle;
    }

    @Override
    public void play() {
        System.out.println("Playing video: " + movieTitle + " in 1080p.");
    }

    @Override
    public void pause() {
        System.out.println("Video paused.");
    }

    @Override
    public void stop() {
        System.out.println("Video stopped.");
    }
}

// Main class to run the program
public class InterfaceDemo {
    public static void main(String[] args) {
        System.out.println("=== Interface Demo ===\n");

        // We can use the interface as a reference type to achieve polymorphism
        Playable myAudio = new AudioPlayer("Bohemian Rhapsody");
        Playable myVideo = new VideoPlayer("Inception");

        System.out.println("--- Audio Player ---");
        myAudio.play();
        myAudio.pause();
        myAudio.stop();

        System.out.println("\n--- Video Player ---");
        myVideo.play();
        myVideo.stop();
    }
}
