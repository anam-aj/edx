describe("flip_coin",{
  it("will print to the console with `cat`", {
    expect_output(cat(flip_coin()))
  })
  it("returns either 'Heads' or 'Tails' for a single flip", {
    result <- flip_coin(1)
    expect_true(result %in% c("Heads", "Tails"))
  })
})