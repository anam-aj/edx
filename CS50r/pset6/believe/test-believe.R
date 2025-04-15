source("believe.R")
library(testthat)

test_that("volume is calculated correctly for numbers", {
  expect_equal(vol_cuboid(c(2, 3, 4)), 24)
})

test_that("volume is calculated correctly for numbers given as string", {
  expect_equal(vol_cuboid(c('2', '3', '4')), 24)
})

test_that("show error for non numeric values", {
  expect_error(vol_cuboid(c("a", 2, 3)))
})

test_that("show error for non missing values", {
  expect_error(vol_cuboid(c(2, 3)))
})


