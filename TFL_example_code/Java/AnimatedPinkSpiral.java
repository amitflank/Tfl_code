import javax.swing.*;
import java.awt.*;
import java.awt.geom.Point2D;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class AnimatedPinkSpiral extends JPanel implements ActionListener {

    private double angleOffset = 0; // Controls the movement of the spiral
    private Timer timer;

    public AnimatedPinkSpiral() {
        // Set up a timer to update the animation every 16ms (~60 frames per second)
        timer = new Timer(16, this);
        timer.start();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawSpiral(g);
    }

    private void drawSpiral(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        // Set the color to pink
        g2d.setColor(Color.PINK);

        int width = getWidth();
        int height = getHeight();
        Point2D.Double center = new Point2D.Double(width / 2, height / 2);

        // Spiral parameters
        double angleIncrement = 0.1;  // Controls how tightly the spiral winds
        double radiusIncrement = 1;   // How fast the radius increases
        double maxAngle = 20 * Math.PI; // Controls how long the spiral is

        double angle = angleOffset;  // The angle now moves over time
        double radius = 0;

        // Draw the spiral
        while (angle < maxAngle + angleOffset) {
            double x = center.x + radius * Math.cos(angle);
            double y = center.y + radius * Math.sin(angle);

            g2d.fillOval((int) x, (int) y, 5, 5); // Draw small circles to form the spiral

            // Increment radius and angle to create the spiral effect
            angle += angleIncrement;
            radius += radiusIncrement;
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // Update the angle offset to make the spiral move
        angleOffset += 0.05; // Adjust this value to control the speed of movement

        // Redraw the panel with the updated angle
        repaint();
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Animated Pink Spiral Pattern");
        AnimatedPinkSpiral panel = new AnimatedPinkSpiral();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(800, 800);
        frame.add(panel);
        frame.setVisible(true);
    }
}
