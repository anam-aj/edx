#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Calculate avg colour value for ([i][j)th pixel(target pixel)
            float avg = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;

            int round_avg = (int) round(avg);

            // Change the colour value for ([i][j])th pixel(target pixel)
            image[i][j].rgbtBlue = round_avg;
            image[i][j].rgbtGreen = round_avg;
            image[i][j].rgbtRed = round_avg;
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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    // Creates a copy of image(2D- Array) to update edges info
    RGBTRIPLE cpy_image[height][width];

    // Loops through every pixel in 2D-array image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

            // Varibles to keep track of weighted sum for each colour(BGR)
            int sum_Bl_Gx = 0;
            int sum_Gr_Gx = 0;
            int sum_Re_Gx = 0;
            int sum_Bl_Gy = 0;
            int sum_Gr_Gy = 0;
            int sum_Re_Gy = 0;

            // Add colour value of valid pixel from (i - 1)th row(Top)
            if (i - 1 >= 0)
            {
                // Top left
                if (j - 1 >= 0)
                {
                    // Updates the sum Gx for respective colours(BGR)
                    sum_Bl_Gx += -1 * image[i - 1][j - 1].rgbtBlue;
                    sum_Gr_Gx += -1 * image[i - 1][j - 1].rgbtGreen;
                    sum_Re_Gx += -1 * image[i - 1][j - 1].rgbtRed;

                    // Updates the sum Gy for respective colours(BGR)
                    sum_Bl_Gy += -1 * image[i - 1][j - 1].rgbtBlue;
                    sum_Gr_Gy += -1 * image[i - 1][j - 1].rgbtGreen;
                    sum_Re_Gy += -1 * image[i - 1][j - 1].rgbtRed;
                }

                // Top centre
                {
                    // Updates the sum Gx for respective colours(BGR)
                    sum_Bl_Gx += 0 * image[i - 1][j].rgbtBlue;
                    sum_Gr_Gx += 0 * image[i - 1][j].rgbtGreen;
                    sum_Re_Gx += 0 * image[i - 1][j].rgbtRed;

                    // Updates the sum Gy for respective colours(BGR)
                    sum_Bl_Gy += -2 * image[i - 1][j].rgbtBlue;
                    sum_Gr_Gy += -2 * image[i - 1][j].rgbtGreen;
                    sum_Re_Gy += -2 * image[i - 1][j].rgbtRed;
                }

                // Top right
                if (j + 1 < width)
                {
                    // Updates the sum Gx for respective colours(BGR)
                    sum_Bl_Gx += 1 * image[i - 1][j + 1].rgbtBlue;
                    sum_Gr_Gx += 1 * image[i - 1][j + 1].rgbtGreen;
                    sum_Re_Gx += 1 * image[i - 1][j + 1].rgbtRed;

                    // Updates the sum Gy for respective colours(BGR)
                    sum_Bl_Gy += -1 * image[i - 1][j + 1].rgbtBlue;
                    sum_Gr_Gy += -1 * image[i - 1][j + 1].rgbtGreen;
                    sum_Re_Gy += -1 * image[i - 1][j + 1].rgbtRed;
                }
            }

            // Add colour value of valid pixel from (i)th row(Centre)

            // Left(of target pixel)
            if (j - 1 >= 0)
            {
                // Updates the sum Gx for respective colours(BGR)
                sum_Bl_Gx += -2 * image[i][j - 1].rgbtBlue;
                sum_Gr_Gx += -2 * image[i][j - 1].rgbtGreen;
                sum_Re_Gx += -2 * image[i][j - 1].rgbtRed;

                // Updates the sum Gy for respective colours(BGR)
                sum_Bl_Gy += 0 * image[i][j - 1].rgbtBlue;
                sum_Gr_Gy += 0 * image[i][j - 1].rgbtGreen;
                sum_Re_Gy += 0 * image[i][j - 1].rgbtRed;
            }

            // Centre(target pixel)
            {
                // Updates the sum Gx for respective colours(BGR)
                sum_Bl_Gx += 0 * image[i][j].rgbtBlue;
                sum_Gr_Gx += 0 * image[i][j].rgbtGreen;
                sum_Re_Gx += 0 * image[i][j].rgbtRed;

                // Updates the sum Gy for respective colours(BGR)
                sum_Bl_Gy += 0 * image[i][j].rgbtBlue;
                sum_Gr_Gy += 0 * image[i][j].rgbtGreen;
                sum_Re_Gy += 0 * image[i][j].rgbtRed;
            }

            // Right(of target pixel)
            if (j + 1 < width)
            {
                // Updates the sum Gx for respective colours(BGR)
                sum_Bl_Gx += 2 * image[i][j + 1].rgbtBlue;
                sum_Gr_Gx += 2 * image[i][j + 1].rgbtGreen;
                sum_Re_Gx += 2 * image[i][j + 1].rgbtRed;

                // Updates the sum Gy for respective colours(BGR)
                sum_Bl_Gy += 0 * image[i][j + 1].rgbtBlue;
                sum_Gr_Gy += 0 * image[i][j + 1].rgbtGreen;
                sum_Re_Gy += 0 * image[i][j + 1].rgbtRed;
            }

            // Add colour value of valid pixel from (i + 1)th row(bottom)
            if (i + 1 < height)
            {
                // Bottom left
                if (j - 1 >= 0)
                {
                    // Updates the sum Gx for respective colours(BGR)
                    sum_Bl_Gx += -1 * image[i + 1][j - 1].rgbtBlue;
                    sum_Gr_Gx += -1 * image[i + 1][j - 1].rgbtGreen;
                    sum_Re_Gx += -1 * image[i + 1][j - 1].rgbtRed;

                    // Updates the sum Gy for respective colours(BGR)
                    sum_Bl_Gy += 1 * image[i + 1][j - 1].rgbtBlue;
                    sum_Gr_Gy += 1 * image[i + 1][j - 1].rgbtGreen;
                    sum_Re_Gy += 1 * image[i + 1][j - 1].rgbtRed;
                }

                // Bottom center
                {
                    // Updates the sum Gx for respective colours(BGR)
                    sum_Bl_Gx += 0 * image[i + 1][j].rgbtBlue;
                    sum_Gr_Gx += 0 * image[i + 1][j].rgbtGreen;
                    sum_Re_Gx += 0 * image[i + 1][j].rgbtRed;

                    // Updates the sum Gy for respective colours(BGR)
                    sum_Bl_Gy += 2 * image[i + 1][j].rgbtBlue;
                    sum_Gr_Gy += 2 * image[i + 1][j].rgbtGreen;
                    sum_Re_Gy += 2 * image[i + 1][j].rgbtRed;
                }

                // Bottom right
                if (j + 1 < width)
                {
                    // Updates the sum Gx for respective colours(BGR)
                    sum_Bl_Gx += 1 * image[i + 1][j + 1].rgbtBlue;
                    sum_Gr_Gx += 1 * image[i + 1][j + 1].rgbtGreen;
                    sum_Re_Gx += 1 * image[i + 1][j + 1].rgbtRed;

                    // Updates the sum Gy for respective colours(BGR)
                    sum_Bl_Gy += 1 * image[i + 1][j + 1].rgbtBlue;
                    sum_Gr_Gy += 1 * image[i + 1][j + 1].rgbtGreen;
                    sum_Re_Gy += 1 * image[i + 1][j + 1].rgbtRed;
                }
            }

            // Calculate Final colour value from weighted sum
            float SqSum_Gx_Gy_Bl = (float)((sum_Bl_Gx * sum_Bl_Gx) + (sum_Bl_Gy * sum_Bl_Gy));
            float SqSum_Gx_Gy_Gr = (float)((sum_Gr_Gx * sum_Gr_Gx) + (sum_Gr_Gy * sum_Gr_Gy));
            float SqSum_Gx_Gy_Re = (float)((sum_Re_Gx * sum_Re_Gx) + (sum_Re_Gy * sum_Re_Gy));

            int Blu = (int) round(sqrt(SqSum_Gx_Gy_Bl));
            int Gre = (int) round(sqrt(SqSum_Gx_Gy_Gr));
            int Red = (int) round(sqrt(SqSum_Gx_Gy_Re));

            // Adds corresponding pixel's colour info in cpy_image
            // BLUE
            if (Blu > 255)
            {
                cpy_image[i][j].rgbtBlue = 255;
            }
            else
            {
                cpy_image[i][j].rgbtBlue = Blu;
            }

            // GREEN
            if (Gre > 255)
            {
                cpy_image[i][j].rgbtGreen = 255;
            }
            else
            {
                cpy_image[i][j].rgbtGreen = Gre;
            }

            // RED
            if (Red > 255)
            {
                cpy_image[i][j].rgbtRed = 255;
            }
            else
            {
                cpy_image[i][j].rgbtRed = Red;
            }
        }
    }

    // Makes desired changes to image
    // by copying pixels' info from cpy_image to image
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
