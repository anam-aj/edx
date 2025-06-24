describe("roll_dice",{
  it("will print to the console with `cat`", {
    expect_output(cat(roll_dice()))
  })
  it("returns two numbers separated by a space for two dice", {
    result <- roll_dice(2)
    parts <- strsplit(result, " ")[[1]]
    expect_equal(length(parts), 2)
    expect_true(all(parts %in% c("1", "2", "3", "4", "5", "6")))
  })
  it("returns three numbers separated by a space for three dice", {
    result <- roll_dice(3)
    parts <- strsplit(result, " ")[[1]]
    expect_equal(length(parts), 3)
    expect_true(all(parts %in% c("1", "2", "3", "4", "5", "6")))
  })
})