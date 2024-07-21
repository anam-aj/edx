#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float avg = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;
            int round_avg = (int) round(avg);
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
            float sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;
            int round_sepiaBlue = (int) round(sepiaBlue);

            float sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            int round_sepiaGreen = (int) round(sepiaGreen);

            float sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            int round_sepiaRed = (int) round(sepiaRed);

            if (round_sepiaBlue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = round_sepiaBlue;
            }

            if (round_sepiaGreen > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = round_sepiaGreen;
            }

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
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, mid = width / 2; j < mid; j++)
        {
            int temp;

            temp = image[i][j].rgbtBlue;
            image[i][j].rgbtBlue = image[i][(width - j)].rgbtBlue;
            image[i][(width - j)].rgbtBlue = temp;

            temp = image[i][j].rgbtGreen;
            image[i][j].rgbtGreen = image[i][(width - j)].rgbtGreen;
            image[i][(width - j)].rgbtGreen = temp;

            temp = image[i][j].rgbtRed;
            image[i][j].rgbtRed = image[i][(width - j)].rgbtRed;
            image[i][(width - j)].rgbtRed = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    RGBTRIPLE cpy_image[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sum = 0;

            if (i - 1 >= 0)
            {
                if (j - 1 >= 0)
                {
                    sum += image[i - 1][j - 1].rgbtBlue;
                }

                sum += image[i - 1][j].rgbtBlue;

                if (j + 1 >= 0)
                {
                    sum += image[i - 1][j + 1].rgbtBlue;
                }
            }
            
            if (i - 1 >= 0)
            {
                if (j - 1 >= 0)
                {
                    sum += image[i - 1][j - 1].rgbtBlue;
                }

                sum += image[i - 1][j].rgbtBlue;

                if (j + 1 >= 0)
                {
                    sum += image[i - 1][j + 1].rgbtBlue;
                }


            }
        }
    }
    return;
}
