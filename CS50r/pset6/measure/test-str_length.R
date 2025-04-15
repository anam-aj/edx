library(stringr)
library(testthat)

test_that("str_length counts alphabets correctly", {
    expect_equal(str_length("abc"), 3)
})

test_that("str_length counts numeric character correctly", {
    expect_equal(str_length("123"), 3)
    expect_equal(str_length("123abc"), 6)
})

test_that("str_length counts special character correctly", {
    expect_equal(str_length("!@#"), 3)
    expect_equal(str_length("abc!@#"), 6)
    expect_equal(str_length("a!b#c%"), 6)
})

test_that("str_length counts spaces correctly", {
    expect_equal(str_length(" abc"), 4)
    expect_equal(str_length(" ab "), 4)
    expect_equal(str_length(" a b"), 4)

})
