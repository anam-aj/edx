#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Calculate avg colour value for ([i][j)th pixel
            float avg = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;
            int round_avg = (int) round(avg);

            // Change the colour value for ([i][j])th pixel
            image[i][j].rgbtBlue = round_avg;
            image[i][j].rgbtGreen = round_avg;
            image[i][j].rgbtRed = round_avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Generates the BGR value as per sepia, for ([i][j])th pixel
            float sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen +
                              .131 * image[i][j].rgbtBlue;

            int round_sepiaBlue = (int) round(sepiaBlue);

            float sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen +
                               .168 * image[i][j].rgbtBlue;

            int round_sepiaGreen = (int) round(sepiaGreen);

            float sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen +
                             .189 * image[i][j].rgbtBlue;

            int round_sepiaRed = (int) round(sepiaRed);

            // Change the ([i][j])th pixel with sepia colour value

            // Blue
            if (round_sepiaBlue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = round_sepiaBlue;
            }

            // Green
            if (round_sepiaGreen > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = round_sepiaGreen;
            }

            // Red
            if (round_sepiaRed > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = round_sepiaRed;
            }
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Horizontally swaps pixels one by one from left
    // with their corresponding pixels from right
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, mid = width / 2; j < mid; j++)
        {
            int temp;

            // Swaps Blue colour
            temp = image[i][j].rgbtBlue;
            image[i][j].rgbtBlue = image[i][(width - 1 - j)].rgbtBlue;
            image[i][(width - 1 - j)].rgbtBlue = temp;

            // Swaps Green colour
            temp = image[i][j].rgbtGreen;
            image[i][j].rgbtGreen = image[i][(width - 1 - j)].rgbtGreen;
            image[i][(width - 1 - j)].rgbtGreen = temp;

            // Swaps Red colour
            temp = image[i][j].rgbtRed;
            image[i][j].rgbtRed = image[i][(width - 1 - j)].rgbtRed;
            image[i][(width - 1 - j)].rgbtRed = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Creates a copy of image to update blur info
    RGBTRIPLE cpy_image[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sum_Bl = 0;
            int sum_Gr = 0;
            int sum_Re = 0;
            float count = 0;

            // Add colour value of valid pixel from (i - 1)th row(Top)
            if (i - 1 >= 0)
            {
                // Top left
                if (j - 1 >= 0)
                {
                    sum_Bl += image[i - 1][j - 1].rgbtBlue;
                    sum_Gr += image[i - 1][j - 1].rgbtGreen;
                    sum_Re += image[i - 1][j - 1].rgbtRed;
                    count++;
                }

                // Top centre
                {
                    sum_Bl += image[i - 1][j].rgbtBlue;
                    sum_Gr += image[i - 1][j].rgbtGreen;
                    sum_Re += image[i - 1][j].rgbtRed;
                    count++;
                }

                // Top right
                if (j + 1 < width)
                {
                    sum_Bl += image[i - 1][j + 1].rgbtBlue;
                    sum_Gr += image[i - 1][j + 1].rgbtGreen;
                    sum_Re += image[i - 1][j + 1].rgbtRed;
                    count++;
                }
            }

            // Add colour value of valid pixel from (i)th row(Centre)
            // Left
            if (j - 1 >= 0)
            {
                sum_Bl += image[i][j - 1].rgbtBlue;
                sum_Gr += image[i][j - 1].rgbtGreen;
                sum_Re += image[i][j - 1].rgbtRed;
                count++;
            }

            // Centre
            {
                sum_Bl += image[i][j].rgbtBlue;
                sum_Gr += image[i][j].rgbtGreen;
                sum_Re += image[i][j].rgbtRed;
                count++;
            }

            // Right
            if (j + 1 < width)
            {
                sum_Bl += image[i][j + 1].rgbtBlue;
                sum_Gr += image[i][j + 1].rgbtGreen;
                sum_Re += image[i][j + 1].rgbtRed;
                count++;
            }

            // Add colour value of valid pixel from (i + 1)th row(bottom)
            if (i + 1 < height)
            {
                // Bottom left
                if (j - 1 >= 0)
                {
                    sum_Bl += image[i + 1][j - 1].rgbtBlue;
                    sum_Gr += image[i + 1][j - 1].rgbtGreen;
                    sum_Re += image[i + 1][j - 1].rgbtRed;
                    count++;
                }

                // Bottom center
                {
                    sum_Bl += image[i + 1][j].rgbtBlue;
                    sum_Gr += image[i + 1][j].rgbtGreen;
                    sum_Re += image[i + 1][j].rgbtRed;
                    count++;
                }

                // Bottom right
                if (j + 1 < width)
                {
                    sum_Bl += image[i + 1][j + 1].rgbtBlue;
                    sum_Gr += image[i + 1][j + 1].rgbtGreen;
                    sum_Re += image[i + 1][j + 1].rgbtRed;
                    count++;
                }
            }

            // Average of colours of valid surrounding pixels
            int avg_Bl = (int) round(sum_Bl / count);
            int avg_Gr = (int) round(sum_Gr / count);
            int avg_Re = (int) round(sum_Re / count);

            // Creates corresponding blurred pixel in copy of image
            cpy_image[i][j].rgbtBlue = avg_Bl;
            cpy_image[i][j].rgbtGreen = avg_Gr;
            cpy_image[i][j].rgbtRed = avg_Re;
        }
    }

    // Copy pixels from blurred copy to original image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtBlue = cpy_image[i][j].rgbtBlue;
            image[i][j].rgbtGreen = cpy_image[i][j].rgbtGreen;
            image[i][j].rgbtRed = cpy_image[i][j].rgbtRed;
        }
    }
    return;
}
