describe("generate_password",{
  it("will print to the console with `cat`", {
    expect_output(cat(generate_password()))
  })
})