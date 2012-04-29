from pyvows import Vows, expect

@Vows.batch
class Boolean(Vows.Context):

    class WhenTrue(Vows.Context):

        def topic(self):
            return True

        def expect_to_be_true(self, topic):
            expect(topic).to_be_true()

        def expect_not_to_be_false(self, topic):
            expect(not topic).to_be_false()
